#!/usr/bin/env node

/**
 * Agent Anti-Hallucination Test Runner
 * 
 * Validates that all agent files comply with anti-hallucination standards.
 */

const fs = require('fs');
const path = require('path');

const AGENTS_DIR = path.join(__dirname, '..', 'agents');
const TESTS_DIR = __dirname;

const REQUIRED_SECTIONS = [
  'ANTI-HALLUCINATION STANDARD',
  'GLOBAL ANTI-HALLUCINATION RULES',
  'Priority order:',
  'Accuracy > Determinism',
];

const REQUIRED_PATTERNS = [
  /Accuracy.*Determinism.*Completeness.*Speed/i,
  /BLOCKED:.*Missing/i,
];

// Agents that don't have traditional "Output format" section
const NO_OUTPUT_FORMAT = ['rapid-prototyper'];

let passed = 0;
let failed = 0;
const errors = [];

function checkAgent(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  const fileName = path.basename(filePath, '.md');
  const relativePath = path.relative(AGENTS_DIR, filePath);
  
  // Skip orchestrator (primary agent - different structure)
  if (fileName === 'orchestrator') {
    console.log(`  ⏭️  ${relativePath} (primary agent - skipped)`);
    passed++;
    return;
  }
  
  // Check for required sections
  const missingSections = REQUIRED_SECTIONS.filter(section => !content.includes(section));
  
  // Check for required patterns
  let missingPatterns = REQUIRED_PATTERNS.filter(pattern => !pattern.test(content));
  
  // Special handling for rapid-prototyper - it has "Guessing is NOT allowed" instead of DO NOT
  if (fileName === 'rapid-prototyper') {
    if (!content.includes('NOT allowed')) {
      missingPatterns.push('NOT allowed (rapid-prototyper specific)');
    }
  } else if (!content.includes('DO NOT')) {
    // Other agents should have "DO NOT" in rules
    if (!content.match(/Rules:[\s\S]*?- DO NOT/i)) {
      missingPatterns.push('DO NOT in rules');
    }
  }
  
  // Check for output format (except rapid-prototyper)
  if (!NO_OUTPUT_FORMAT.includes(fileName)) {
    if (!content.includes('Output format:') && !content.includes('Output Format:')) {
      missingPatterns.push('Output format section');
    }
  }
  
  if (missingSections.length === 0 && missingPatterns.length === 0) {
    console.log(`  ✅ ${relativePath}`);
    passed++;
  } else {
    console.log(`  ❌ ${relativePath}`);
    if (missingSections.length > 0) {
      errors.push(`  Missing sections in ${relativePath}:`);
      missingSections.forEach(s => errors.push(`    - ${s}`));
    }
    if (missingPatterns.length > 0) {
      errors.push(`  Missing patterns in ${relativePath}:`);
      missingPatterns.forEach(p => errors.push(`    - ${p}`));
    }
    failed++;
  }
}

function checkAllAgents() {
  console.log('🧪 Running Anti-Hallucination Tests\n');
  console.log('📁 Checking agents in:', AGENTS_DIR);
  console.log('');
  
  const files = fs.readdirSync(AGENTS_DIR)
    .filter(f => f.endsWith('.md'))
    .map(f => path.join(AGENTS_DIR, f));
  
  files.forEach(checkAgent);
  
  console.log('\n' + '='.repeat(50));
  console.log(`Results: ${passed} passed, ${failed} failed`);
  console.log('='.repeat(50));
  
  if (errors.length > 0) {
    console.log('\n❌ Errors:');
    errors.forEach(e => console.log(e));
  }
  
  if (failed > 0) {
    console.log('\n💥 Some tests failed!');
    process.exit(1);
  } else {
    console.log('\n✅ All anti-hallucination tests passed!');
  }
}

function checkSkillsDirectory() {
  console.log('\n📦 Checking skills directory...');
  
  const skillsDir = path.join(__dirname, '..', 'skills', 'individual');
  
  if (!fs.existsSync(skillsDir)) {
    console.log('  ⚠️  Skills directory not found');
    return;
  }
  
  const skills = fs.readdirSync(skillsDir).filter(f => fs.statSync(path.join(skillsDir, f)).isDirectory());
  console.log(`  ✅ Found ${skills.length} skills`);
  
  // Check for README in skills
  const readmeCount = skills.filter(s => {
    const readmePath = path.join(skillsDir, s, 'README.md');
    return fs.existsSync(readmePath);
  }).length;
  
  console.log(`  📝 ${readmeCount} skills have README.md`);
  
  if (readmeCount < skills.length * 0.5) {
    console.log('  ⚠️  Less than 50% of skills have README.md');
  }
}

function checkAgentConsistency() {
  console.log('\n🔍 Checking agent consistency...');
  
  const files = fs.readdirSync(AGENTS_DIR)
    .filter(f => f.endsWith('.md') && f !== 'orchestrator.md');
  
  let hasBlockResponse = 0;
  let hasStructuredOutput = 0;
  let hasExecutionMode = 0;
  let hasAntiHallucination = 0;
  let hasRules = 0;
  
  files.forEach(file => {
    const content = fs.readFileSync(path.join(AGENTS_DIR, file), 'utf8');
    if (content.includes('BLOCKED: Missing')) hasBlockResponse++;
    if (content.includes('Output format:') || content.includes('Output Format:')) hasStructuredOutput++;
    if (content.includes('PHASE') || content.includes('Execution Mode')) hasExecutionMode++;
    if (content.includes('ANTI-HALLUCINATION')) hasAntiHallucination++;
    if (content.includes('Rules:')) hasRules++;
  });
  
  console.log(`  Block responses: ${hasBlockResponse}/${files.length}`);
  console.log(`  Structured outputs: ${hasStructuredOutput}/${files.length}`);
  console.log(`  Execution modes: ${hasExecutionMode}/${files.length}`);
  console.log(`  Anti-hallucination sections: ${hasAntiHallucination}/${files.length}`);
  console.log(`  Rules sections: ${hasRules}/${files.length}`);
  
  if (hasBlockResponse === files.length && 
      hasStructuredOutput + NO_OUTPUT_FORMAT.length >= files.length && 
      hasExecutionMode === files.length &&
      hasAntiHallucination === files.length &&
      hasRules === files.length) {
    console.log('  ✅ All agents are consistent');
  } else {
    console.log('  ⚠️  Some inconsistencies detected');
  }
}

function checkAGENTSDoc() {
  console.log('\n📄 Checking AGENTS.md...');
  
  const agentsMdPath = path.join(__dirname, '..', 'AGENTS.md');
  if (fs.existsSync(agentsMdPath)) {
    const content = fs.readFileSync(agentsMdPath, 'utf8');
    const agentCount = (content.match(/### /g) || []).length;
    console.log(`  ✅ AGENTS.md exists with ${agentCount} agent entries`);
  } else {
    console.log('  ⚠️  AGENTS.md not found');
  }
}

function checkTestsExist() {
  console.log('\n🧪 Checking tests...');
  
  const testFiles = fs.readdirSync(TESTS_DIR).filter(f => f.endsWith('.js') || f.endsWith('.md'));
  console.log(`  ✅ Found ${testFiles.length} test files`);
  
  if (testFiles.includes('test-runner.js') && testFiles.includes('README.md')) {
    console.log('  ✅ Test infrastructure complete');
  }
}

function runAllTests() {
  checkAllAgents();
  checkSkillsDirectory();
  checkAgentConsistency();
  checkAGENTSDoc();
  checkTestsExist();
}

// Run tests
runAllTests();
