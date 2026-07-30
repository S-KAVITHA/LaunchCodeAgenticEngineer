Trigger: A developer invokes claude "[task prompt]" from the repo root.

If the Docker build succeeds, the agent summarizes any warnings and recommends
proceeding.

If the Docker build fails, the agent reports the error output and recommends
against proceeding. It does not attempt a fix.

Read the repository’s documentation to identify the documented Docker build
command.

Run the Docker build command inside the sandbox.

Capture the output from the build process.

Evaluate the build result (success or failure).

Summarize any warnings or errors present in the output.

Produce a final recommendation, ready to proceed or not ready, with a brief
rationale.


The agent correctly identifies whether the Docker image was built successfully or failed.

The summary includes all warnings and errors present in the build output; it
does not omit any.

The recommendation is consistent with the build result.

The agent did not push, publish, or deploy anything.
