
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

