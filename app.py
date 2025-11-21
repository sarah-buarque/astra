from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "segredo123"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")

        # Autenticação fictícia (troque por banco de dados)
        if usuario == "admin" and senha == "123":
            return "Login realizado com sucesso!"

        flash("Usuário ou senha incorretos!")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/recuperar-senha")
def recuperar_senha():
    return render_template("recuperarsenha.html")


@app.route("/cadastro")
def cadastro():
    return "<h2>Página de cadastro</h2>"


if __name__ == "__main__":
    app.run(debug=True)

