from flask import Flask, jsonify, request
import repository

#Créer l'application
app = Flask(__name__)

#Définir les routes
@app.route("/")
def home():
        return "C'est cool REST !"

@app.route("/students", methods=["GET"])
def get_students():
    students=repository.get_all_students()
    return jsonify(students), 200

@app.route("/students/<INT:student_id>", methods=["GET"])
def get_student_by_id(student_id):
    student=repository.get_student_by_id(student_id)
    return jsonify(student), 200

#Lancer le serveur
#Force Flask à écouter sur toutes les interfaces IPV4 + IPV6) :
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
