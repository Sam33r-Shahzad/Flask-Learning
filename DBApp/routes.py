from flask import render_template, request
from models import Person

def register_routes(app, db):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            return render_template('index.html', people=people)

        elif request.method == 'POST':
            name = request.form.get('name')
            age = int(request.form.get('age'))
            job = request.form.get('job')

            # Create new Person Object
            new_person = Person(name=name, age=age, job=job)

            # Save to Database
            db.session.add(new_person)
            db.session.commit()

            people = Person.query.all()
            return render_template('index.html', people=people)


    @app.route('/delete/<int:p_id>', methods=['DELETE'])
    def delete(p_id):
        Person.query.filter(Person.p_id == p_id).delete()
        db.session.commit()

        people = Person.query.all()
        return render_template('index.html', people=people)


    @app.route('/details/<int:p_id>', methods=['GET'])
    def details(p_id):

        person = Person.query.filter(Person.p_id == p_id).first()
        return render_template('detail.html', person=person)