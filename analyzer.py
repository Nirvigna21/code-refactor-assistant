import ast

def analyze_code(code):
    issues = []
    suggestions = []

    try:
        tree = ast.parse(code)
    except:
        return {
            "issues": ["Invalid Python code."],
            "suggestions": []
        }

    # Check long functions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if len(node.body) > 30:
                issues.append(f"Function '{node.name}' is too long.")
                suggestions.append("Break the function into smaller helper functions.")

            if len(node.args.args) > 4:
                issues.append(f"Function '{node.name}' has too many parameters.")
                suggestions.append("Reduce parameters or use a config object.")

    # Check nested loops
    for node in ast.walk(tree):
        if isinstance(node, (ast.For, ast.While)):
            for child in ast.walk(node):
                if isinstance(child, (ast.For, ast.While)) and child != node:
                    issues.append("Nested loop detected (O(n²) risk).")
                    suggestions.append("Use dictionary or set for faster lookup.")
                    break

    # Check bad variable names
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if len(node.id) == 1 and node.id not in ['i', 'j']:
                issues.append(f"Variable '{node.id}' is not descriptive.")
                suggestions.append("Use meaningful variable names.")

    if not issues:
        issues.append("No major structural issues detected.")
        suggestions.append("Code structure looks clean.")

    return {
        "issues": list(set(issues)),
        "suggestions": list(set(suggestions))
    }
