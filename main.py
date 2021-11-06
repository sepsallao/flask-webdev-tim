from website import create_app

app = create_app()

if __name__ == '__main__':  # only if we run this file, not if we import this line
    app.run(debug=True)
