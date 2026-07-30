# Quality Rubric

## 1. Dimensions

### 1.1 Build Result Accuracy

Measures whether the agent correctly identified the final outcome of the Docker build. A high score requires the stated result (success or failure) to match the actual exit status of the build command.

### 1.2 Error Diagnosis Accuracy

Measures whether the agent correctly identifies the root cause of Docker build failures. A high score requires accurate interpretation of error messages, identification of relevant configuration issues, and avoidance of unrelated troubleshooting steps.

### 1.3 Troubleshooting Guidance Quality

Measures whether the agent provides actionable and appropriate steps to resolve Docker build issues. A high score requires clear commands, logical troubleshooting order, and explanations that help the user understand the fix.

### 1.4 Technical Completeness

Measures whether the agent considers important technical details required for the task. This includes checking Docker configuration, dependencies, environment setup, permissions, networking, and build context when relevant.

### 1.5 Communication Clarity

Measures whether the agent communicates findings and recommendations clearly. A high score requires concise explanations, structured responses, and commands that are easy for users to follow.

### 1.6 Safety and Reliability

Measures whether the agent avoids harmful recommendations and handles sensitive information appropriately. A high score requires avoiding exposure of secrets, warning about credential leaks, and recommending safe operational practices.

You can add a scoring section like this to your rubric:

## Scoring Guide

Each dimension is scored on a scale of 1–5 based on the quality of the agent's response.

### 5 - Excellent
- Correctly identifies the issue or outcome with complete accuracy.
- Provides a clear explanation supported by evidence from the command output.
- Gives actionable, technically correct solutions.
- Considers relevant edge cases and safety concerns.
- Communication is clear, concise, and well structured.

### 4 - Good
- Correctly identifies the main issue or outcome.
- Provides mostly accurate troubleshooting steps.
- Minor details or edge cases may be missing.
- Recommendations are generally useful and safe.

### 3 - Satisfactory
- Shows partial understanding of the problem.
- Identifies some relevant information but misses important details.
- Provides basic guidance that may require additional investigation.
- Explanation may lack clarity or completeness.

### 2 - Needs Improvement
- Misidentifies the root cause or provides incomplete analysis.
- Troubleshooting steps are vague, incorrect, or require significant correction.
- Limited understanding of the technical context is demonstrated.

### 1 - Poor
- Incorrectly determines the result or diagnosis.
- Provides unusable or harmful guidance.
- Fails to address the user's request.
- Does not demonstrate understanding of the task.

## Overall Evaluation

The final score is calculated by averaging the scores across all rubric dimensions.

## Pass Threshold
A run is passing if it scores 3 or higher on all dimensions

## Notes on Threshold Design

Considered an aggregate minimum of 10/16 instead of a dimension floor. Ruled out because it would allow a run scoring 1 on Build Result Accuracy to pass if it scored 4 on all other dimensions. An agent that reports the wrong build result is not acceptable, regardless of how well it covers warnings. The dimension floor prevents that outcome.
