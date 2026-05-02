"""
Sanitized reference accessibility issue classifier.

This file is for portfolio demonstration only.
It does not include production source code, proprietary AI logic,
reverse-engineering methods, customer documents, prompts, validators,
or commercial accessibility automation workflows.
"""


def classify_issue(issue_type):
    issue_type = issue_type.lower().strip()

    severity_map = {
        "missing alt text": "moderate",
        "incorrect reading order": "critical",
        "missing document language": "moderate",
        "untagged table": "critical",
        "missing form label": "critical",
        "heading hierarchy issue": "moderate",
        "artifact tagging issue": "minor",
    }

    return severity_map.get(issue_type, "review_required")


def recommend_action(issue_type):
    issue_type = issue_type.lower().strip()

    recommendations = {
        "missing alt text": "Add meaningful alternative text that describes the purpose of the image.",
        "incorrect reading order": "Review and correct the logical reading order for assistive technologies.",
        "missing document language": "Set the document language metadata.",
        "untagged table": "Add table structure tags and verify header relationships.",
        "missing form label": "Associate the form field with a clear accessible label.",
        "heading hierarchy issue": "Review heading levels and correct the semantic hierarchy.",
        "artifact tagging issue": "Mark decorative or non-meaningful elements as artifacts.",
    }

    return recommendations.get(issue_type, "Send this issue for accessibility review.")


if __name__ == "__main__":
    sample_issue = "Missing Alt Text"

    print({
        "issueType": sample_issue,
        "severity": classify_issue(sample_issue),
        "recommendedAction": recommend_action(sample_issue),
    })
