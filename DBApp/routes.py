# from flask import render_template, request
# from models import Person

# def register_routes(app, db):

#     @app.route('/', methods=['GET', 'POST'])
#     def index():
#         if request.method == 'GET':
#             people = Person.query.all()
#             return render_template('index.html', people=people)

#         elif request.method == 'POST':
#             name = request.form.get('name')
#             age = int(request.form.get('age'))
#             job = request.form.get('job')

#             # Create new Person Object
#             new_person = Person(name=name, age=age, job=job)

#             # Save to Database
#             db.session.add(new_person)
#             db.session.commit()

#             people = Person.query.all()
#             return render_template('index.html', people=people)


#     @app.route('/delete/<int:p_id>', methods=['DELETE'])
#     def delete(p_id):
#         Person.query.filter(Person.p_id == p_id).delete()
#         db.session.commit()

#         people = Person.query.all()
#         return render_template('index.html', people=people)


#     @app.route('/details/<int:p_id>', methods=['GET'])
#     def details(p_id):

#         person = Person.query.filter(Person.p_id == p_id).first()
#         return render_template('detail.html', person=person)




from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from models import User

def register_routes(app, db, bcrypt):

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            # Hash Password before storing
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('index'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')

        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')

            user = User.query.filter(User.username == username).first()

            # Verify Password Hash
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return "Failed to log in. Invalid Credentials."

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/secret')
    @login_required
    def secret():
        return f"My secret message! Welcome {current_user.username}"