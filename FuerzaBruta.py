import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QLineEdit, QPushButton, QLabel, QTextEdit, QFileDialog,
                           QMessageBox, QGridLayout)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import itertools
import re
#Desarrollado por: Carlitos de la V
#GUI: Rafa Ramos. Coquimbo
class DictionaryGeneratorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Diccionarios")
        self.setMinimumSize(600, 700)
        
         
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # un loguito de la fiscalia para que se vea pulento
        logo_label = QLabel()
        logo = QPixmap("logo.png")
        scaled_logo = logo.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(scaled_logo)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)
        
        
        grid = QGridLayout()
        
        # Campos de entrada
        self.fields = {
            "name": ("Nombres/Apodos:", "Ingrese nombres separados por espacios"),
            "dates": ("Fechas importantes:", "Fechas separadas por espacios (ej: 1990 0412)"),
            "numbers": ("Números de ID:", "DNI, teléfono, etc. separados por espacios"),
            "places": ("Lugares:", "Direcciones o lugares relevantes"),
            "interests": ("Intereses:", "Deportes, mascotas, personajes favoritos"),
            "phrases": ("Frases:", "Palabras o frases comunes"),
        }
        
        self.inputs = {}
        row = 0
        for key, (label_text, placeholder) in self.fields.items():
            label = QLabel(label_text)
            self.inputs[key] = QLineEdit()
            self.inputs[key].setPlaceholderText(placeholder)
            grid.addWidget(label, row, 0)
            grid.addWidget(self.inputs[key], row, 1)
            row += 1
            
        layout.addLayout(grid)
        
        # un espacio para la vista previa
        preview_label = QLabel("Vista previa del diccionario:")
        layout.addWidget(preview_label)
        
        self.preview_area = QTextEdit()
        self.preview_area.setReadOnly(True)
        self.preview_area.setMinimumHeight(150)
        layout.addWidget(self.preview_area)
        
       
        button_layout = QVBoxLayout()
        
        self.generate_button = QPushButton("Generar Vista Previa")
        self.generate_button.clicked.connect(self.preview_dictionary)
        button_layout.addWidget(self.generate_button)
        
        self.save_button = QPushButton("Guardar Diccionario")
        self.save_button.clicked.connect(self.save_dictionary)
        button_layout.addWidget(self.save_button)
        
        self.clear_button = QPushButton("Limpiar Campos")
        self.clear_button.clicked.connect(self.clear_fields)
        button_layout.addWidget(self.clear_button)
        
        layout.addLayout(button_layout)

    def clean_text(self, text):
        return re.sub(r"[ ,./-]", "", text)

    def generate_combinations(self):
        data = {
            key: self.inputs[key].text().split() 
            for key in self.fields.keys()
        }
        data["common_patterns"] = ["1234", "0000", "2580", "1111", "1122"]
        
        all_data = [
            self.clean_text(item) for item in (
                data["name"] +
                data["dates"] +
                data["numbers"] +
                data["places"] +
                data["interests"] +
                data["phrases"] +
                data["common_patterns"]
            )
        ]

        combinations = set()
        for length in range(1, 4):
            for combo in itertools.combinations(all_data, length):
                combined = ''.join(combo)
                combinations.add(combined)
        
        return sorted(combinations)

    def preview_dictionary(self):
        try:
            combinations = self.generate_combinations()
            preview_text = "\n".join(combinations[:100])  # Mostrar solo primeras 100 combinaciones, podrian ser mas, ahi ve usted colega
            if len(combinations) > 100:
                preview_text += f"\n\n... y {len(combinations) - 100} combinaciones más"
            self.preview_area.setText(preview_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al generar vista previa: {str(e)}")

    def save_dictionary(self):
        try:
            combinations = self.generate_combinations()
            filename, _ = QFileDialog.getSaveFileName(
                self,
                "Guardar Diccionario",
                "",
                "Archivos de texto (*.txt)"
            )
            if filename:
                with open(filename, "w", encoding='utf-8') as file:
                    for word in combinations:
                        file.write(f"{word}\n")
                QMessageBox.information(
                    self,
                    "Éxito",
                    f"Diccionario guardado exitosamente en:\n{filename}"
                )
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al guardar el diccionario: {str(e)}")

    def clear_fields(self):
        for input_field in self.inputs.values():
            input_field.clear()
        self.preview_area.clear()

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')   
    window = DictionaryGeneratorGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()