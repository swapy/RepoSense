# Prompt Engineering Guardrails

These guardrails apply to every prompt created under `abilities/prompts/`.
They are the mandatory rules prompt authors must follow.

## Mandatory prompt guardrails

1. No edit policy
   * Prompts may assess, recommend, or describe required changes.
   * Prompts must never instruct the AI to directly modify, generate, or patch repository code.

2. Prompt metadata completeness
   * Every prompt must include required frontmatter fields defined in `docs/prompt-requirements.md` and `abilities/schemas/prompt-metadata.schema.yaml`.
   * Missing required fields invalidate the prompt.

3. Controlled taxonomy
   * Prompt metadata fields such as `pillar`, `capability`, `topic`, `applicable_languages`, `recommended_tools`, `tags`, `confidence`, `status`, and `severity` must use the controlled vocabulary.

4. Evidence-first output
   * Prompts must instruct the AI to cite evidence, such as file paths, line numbers, or relevant configuration snippets.
   * Uncertain findings must be labeled as `Potential` or `Needs verification`.

5. No sensitive data requests
   * Prompts must not request PII, secrets, credentials, or proprietary data from the repository.

6. Scope discipline
   * Each prompt should focus on a single Topic or clearly bounded assessment objective.
   * Avoid broad or ambiguous requests that cover multiple unrelated concerns.

7. Prompt quality
   * Prompts should be clear, concise, and actionable.
   * Prompts should include examples or guidance when needed for interpretation.

8. Testable outputs
   * Prompts should define expected output structure or labels wherever possible.
   * Prompts should be compatible with validation and test harnesses.

## Validation workflow

* Store guardrails in `abilities/prompts/guardrails.md`.
* Define technical validation rules in `abilities/validation/`.
* Require prompt authors to validate new prompt files before merge.
* Keep the guardrails file in sync with `docs/prompt-requirements.md` and `abilities/schemas/prompt-metadata.schema.yaml`.
