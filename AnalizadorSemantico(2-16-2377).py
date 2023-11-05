class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_symbol(self, name, data_type):
        if name in self.symbols:
            print(f"Error semántico: La variable '{name}' ya está declarada.")
        else:
            self.symbols[name] = data_type

    def check_variable(self, name):
        if name not in self.symbols:
            print(f"Error semántico: La variable '{name}' no está declarada.")

def analyze_semantics(ast):
    symbol_table = SymbolTable()

    def traverse(node):
        if node["type"] == "variable_declaration":
            variable_name = node["name"]
            data_type = node["data_type"]
            symbol_table.add_symbol(variable_name, data_type)
        elif node["type"] == "variable_usage":
            variable_name = node["name"]
            symbol_table.check_variable(variable_name)

        for child in node.get("children", []):
            traverse(child)

    traverse(ast)

# Ejemplo de AST (Árbol de Sintaxis Abstracta) simplificado
ast = {
    "type": "program",
    "children": [
        {
            "type": "variable_declaration",
            "name": "x",
            "data_type": "int"
        },
        {
            "type": "variable_usage",
            "name": "y"
        }
    ]
}

# Analizar semántica
analyze_semantics(ast)
