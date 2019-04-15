from app import create_app
from flask_script import Manager, Server

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    '''
    Run unit tests(this feature is the coolest bana)
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
# manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()
