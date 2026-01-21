# Agent Tests

Anti-hallucination validation tests for all specialist agents.

## Running Tests

```bash
# Run all tests
node test-runner.js

# Run with verbose output
node test-runner.js --verbose
```

## Test Categories

### 1. Anti-Hallucination Compliance
Validates that each agent:
- Includes the ANTI-HALLUCINATION STANDARD section
- Has global rules (Accuracy > Determinism > Completeness > Speed)
- Uses BLOCKED responses for missing information
- Returns structured JSON outputs
- Follows the 4-phase execution mode

### 2. Skills Integration
Validates that:
- Skills directory exists at `.opencode/skills/individual/`
- Skills have README.md documentation
- Agent files reference available skills

### 3. Agent Consistency
Validates that:
- All agents have consistent structure
- Required patterns are present in all files
- No agent is missing critical sections

## Test Output

```
🧪 Running Anti-Hallucination Tests

📁 Checking agents in: /path/to/agents

  ✅ frontend-developer.md
  ✅ backend-architect.md
  ✅ ai-engineer.md
  ❌ security-auditor.md

==================================================
Results: 12 passed, 1 failed
==================================================

❌ Errors:
  Missing sections in security-auditor.md:
    - BLOCKED: Missing

💥 Some tests failed!
```

## Adding New Tests

To add a new test:

1. Create a new test function in `test-runner.js`
2. Add validation logic
3. Output results with ✅ or ❌

Example:

```javascript
function myNewTest() {
  console.log('\n🔍 Running my new test...');
  // validation logic
  if (valid) {
    console.log('  ✅ Test passed');
  } else {
    console.log('  ❌ Test failed');
  }
}
```

## CI/CD Integration

Add to your CI pipeline:

```yaml
- name: Run agent tests
  run: node .opencode/tests/test-runner.js
```

## Test Coverage

| Test | Description | Status |
|------|-------------|--------|
| Required Sections | Checks for mandatory markdown sections | ✅ |
| Anti-Hallucination Rules | Validates accuracy > determinism rules | ✅ |
| Block Responses | Confirms BLOCKED format is used | ✅ |
| Structured Output | Validates JSON output format | ✅ |
| Skills Directory | Checks skills are installed | ✅ |
| Agent Consistency | Ensures uniform agent structure | ✅ |
