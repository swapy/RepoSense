# Repo Sense Reporting Requirements

This document defines the report schema, report structure, scoring model, aggregation rules, and global score expectations for Repo Sense.
It is intended to make reporting explicit, standardized, and consistent across output formats.

## Purpose

* Define a standard report schema for assessment output.
* Describe how findings, scores, and evidence are structured.
* Specify scoring rules for Topic, Capability, Pillar, and Global scores.
* Capture how missing data, skipped prompts, and confidence affect scoring.
* Define the expected report shape for JSON, Markdown, and HTML output.

## Report structure

A Repo Sense report should be organized into the following top-level sections:

1. Metadata
2. Executive Summary
3. Scores
4. Detailed Findings
5. General Observations
6. Evidence and References
7. Appendices (optional)

### 1. Metadata

Report metadata should include:

* `report_id`
* `report_version`
* `generated_at`
* `repository_name`
* `repository_path`
* `repo_url` (optional)
* `assessment_scope`
* `selected_pillars`
* `selected_capabilities`
* `selected_topics`
* `report_format`
* `tool_version`
* `analysis_duration`

### 2. Executive Summary

The executive summary should contain:

* overall `global_score`
* a short narrative of the repository health
* highlights of critical issues
* top recommendations
* confidence summary

### 3. Scores

The report should include a hierarchical score breakdown:

* `topic_scores`
* `capability_scores`
* `pillar_scores`
* `global_score`

The score section should also include:

* `score_scale` (for example, 0-100)
* `severity_counts`
* `confidence_distribution`
* `weighting_strategy`

### 4. Detailed Findings

Each finding entry should include:

* `id`
* `pillar`
* `capability`
* `topic`
* `severity`
* `confidence`
* `score_impact`
* `message`
* `recommendation`
* `file_path`
* `line_number`
* `evidence`
* `related_prompts`
* `related_findings`

### 5. General Observations

This section captures high-level risks or patterns that do not fit into a single Pillar or Topic.

* `observation_id`
* `summary`
* `details`
* `recommendation`
* `confidence`

### 6. Evidence and References

Evidence and references should link findings to:

* file paths
* line numbers or code snippets
* commit metadata if available
* prompt names and prompt metadata entries

### 7. Appendices

Optional supplemental content can include:

* glossary
* score definitions
* assessment assumptions
* analysis limitations

## Report schema

The canonical report schema should be defined as a structured JSON object.

### Example schema outline

```json
{
  "report_id": "string",
  "report_version": "string",
  "generated_at": "string",
  "repository_name": "string",
  "repository_path": "string",
  "repo_url": "string",
  "assessment_scope": "string",
  "selected_pillars": ["string"],
  "selected_capabilities": ["string"],
  "selected_topics": ["string"],
  "report_format": "string",
  "tool_version": "string",
  "analysis_duration": "number",
  "score_scale": "string",
  "global_score": "number",
  "pillar_scores": {
    "Security": {"score": 0, "weight": 0.25, "confidence": "string"}
  },
  "capability_scores": {
    "Secret Management": {"score": 0, "pillar": "Security", "confidence": "string"}
  },
  "topic_scores": {
    "Hardcoded Credentials": {"score": 0, "capability": "Secret Management", "pillar": "Security", "confidence": "string"}
  },
  "severity_counts": {
    "critical": 0,
    "high": 0,
    "medium": 0,
    "low": 0
  },
  "confidence_distribution": {
    "high": 0,
    "medium": 0,
    "low": 0
  },
  "findings": [
    {
      "id": "string",
      "pillar": "Security",
      "capability": "Secret Management",
      "topic": "Hardcoded Credentials",
      "severity": "Critical",
      "confidence": "High",
      "score_impact": -10,
      "message": "Hardcoded API key found in config.js",
      "recommendation": "Move the key to a secrets manager and rotate it.",
      "file_path": "config/config.js",
      "line_number": 42,
      "evidence": "exports.API_KEY = 'secret'",
      "related_prompts": ["hardcoded-credential-detection"]
    }
  ],
  "general_observations": [
    {
      "observation_id": "string",
      "summary": "No Azure AD configuration detected",
      "details": "The repository does not contain Azure AD manifest files.",
      "recommendation": "Verify identity provider setup for production deployments.",
      "confidence": "Medium"
    }
  ]
}
```

## Scoring model

### Score range

Use a 0-100 range for all scores.

* 100 = excellent, no findings or risks detected
* 75-99 = good, minor observations
* 50-74 = moderate risk, actionable findings exist
* 25-49 = high risk, many issues or inconsistent practices
* 0-24 = critical risk, urgent remediation required

### Severity mapping

Map findings to score impact by severity:

* Critical = large negative impact
* High = significant negative impact
* Medium = moderate negative impact
* Low = small negative impact

### Confidence labels

Use controlled confidence values:

* `high`
* `medium`
* `low`

### Topic scoring

Each Topic score should reflect the aggregated findings for that Topic.

* Start with a baseline of 100.
* Subtract weighted penalties for each finding.
* Optionally add positive adjustments for best practices or strong evidence.

Example:

* Start = 100
* Critical finding = -20
* High finding = -10
* Medium finding = -5
* Low finding = -2

### Capability scoring

Aggregate Topic scores into Capability scores.

* Capability score = weighted average of its Topic scores.
* Use topic weights when some topics are more important than others.
* If weights are not defined, use equal weighting.

### Pillar scoring

Aggregate Capability scores into Pillar scores.

* Pillar score = weighted average of its Capability scores.
* Use pillar-specific weights for Capabilities when necessary.
* Otherwise, use equal weighting across Capability scores.

### Global score

Compute the Global Repository Score from Pillar scores.

* Global score = weighted average of selected Pillar scores.
* For MVP, use equal weighting across selected Pillars.
* Alternative: weight Pillars by business importance or assessment scope.

Example global score formula:

```
global_score = (sum(pillar_score_i * pillar_weight_i) / sum(pillar_weight_i))
```

If only Security and Observability are selected for launch, then:

```
global_score = (security_score + observability_score) / 2
```

### Handling missing data

* If a Topic has no findings and no coverage, treat it as `not assessed` rather than automatically perfect.
* Use a separate `coverage` marker for Topics and Capabilities.
* If coverage is low, reduce confidence or flag the report as partial.
* Do not penalize missing prompts that were intentionally excluded from the selected scope.

### Confidence aggregation

Aggregate confidence by propagating the lowest confidence from Topic to Capability to Pillar when a finding is uncertain.

Example:

* Topic A = high confidence
* Topic B = medium confidence
* Capability confidence = medium

## Report output shape

### JSON

Use the schema above as the canonical JSON shape.

### Markdown

The Markdown report should mirror the JSON structure with clear sections:

* Executive Summary
* Scoring Table
* Findings Table
* General Observations
* Evidence Summary

### HTML

HTML should render the same sections with visual score cards, tables, and collapsible evidence.

## Recommended report sections

1. Executive Summary
2. Scores by Pillar, Capability, Topic
3. Findings ordered by severity
4. General Observations / unknowns
5. Evidence references
6. Appendix: scoring methodology

## Report generation guidance

* Always generate a `global_score` for the selected assessment scope.
* Include `General Observations` for cross-cutting issues and unknowns.
* Keep the report machine-readable and human-readable.
* Use the same score scale across Topic, Capability, Pillar, and Global scores.

## Open questions

* Should reports also include issue-tracking identifiers for follow-up workflows?
* Should the report schema support multiple component sets in a single assessment?
* Should a partial coverage marker be included in the top-level metadata?
