---
name: test
description: Write comprehensive unit tests for component behavior in isolation
---

<task>
Write comprehensive unit tests for a program that validate behavior in isolation.

Unit tests are executable documentation—they tell the story of what your component does and why. Write tests that validate behavior, not implementation. Cover happy paths, edge cases, error conditions, and all critical business logic.

Follow this process:

1. **Review component specification:**
   - Read source code and documentation to understand functionality
   - Extract all public methods, edge cases, and error conditions to test
   - Ask the user any clarifying questions to resolve ambiguity, prioritize test cases, determine the relevance of edge cases, etc. in an adversarial interview format using the QA engineerersona
2. **Write happy path tests:**
   - Test each public method with typical inputs
   - Verify expected outputs match specification
   - Use realistic data from constellation context

3. **Write edge case tests:**
   - Test boundary conditions (empty, max, min, null)
   - Test unusual but valid inputs
   - Verify graceful handling

4. **Write error condition tests:**
   - Test all error paths
   - Verify error handling per specification
   - Confirm recovery behavior

5. **Write critical logic tests:**
   - Achieve 100% branch coverage of business logic
   - Test all decision paths
   - Verify against gap success criteria
</task>


<thinking>
Before writing tests, analyze:
1. What are ALL public methods that need testing?
2. What edge cases exist (boundary conditions, empty inputs, null values)?
3. What error conditions must be handled?
4. What is the critical business logic that requires 100% coverage?
5. How can tests serve as executable documentation?
</thinking>

<output-format>
Write unit tests using the pytest framework following the python3 and pytest standards and coding patterns:

**Test File Structure Pattern:**

1. **File Header Documentation:**
   - Component under test
   - Purpose statement
   - Specification reference
   - Coverage summary (happy/edge/error/critical)
   - Success criteria being validated

2. **Test Organization:**
   - Group related tests by scenario/feature
   - Use descriptive names that explain behavior
   - Follow AAA pattern (Arrange, Act, Assert)
   - Make tests independent and fast (<100ms each)

3. **Test Categories to Cover:**
   - Happy paths: typical usage with valid inputs
   - Edge cases: boundary conditions (empty, null, max, min)
   - Error conditions: all error paths and recovery

Verify against specification, not just "something happened"
</output-format>

<instructions>
CRITICAL: Write tests as executable documentation that tell the story of what your component does.

NEVER write tests that:
- Test implementation details instead of behavior
- Use vague assertions 
- Skip edge cases or error conditions
- Lack descriptive test names
- Don't validate against specification
- Use unrealistic test data
- Write "test that it works" - be specific about WHAT works
- Skip boundary conditions (null, empty, max, min)
- Forget to test error paths (they MUST be tested)
- Write tests that depend on other tests (tests MUST be independent)
- Skip the critical business logic (100% coverage REQUIRED)
- Use magic numbers without explanation

ALWAYS:
- Write descriptive test names that explain the scenario
- Use AAA pattern (Arrange, Act, Assert)
- Test behavior, not implementation
- Use realistic data from constellation context
- Test ALL edge cases and boundary conditions
- Test ALL error conditions and recovery
- Achieve 100% branch coverage of critical business logic
- Make tests fast (unit tests MUST be < 100ms)
- Make tests independent (no order dependencies)
- Validate against gap success criteria

REPEAT: Tests are executable documentation. Every test name should read like a specification. Use realistic data. Test behavior, not implementation. 
</instructions>