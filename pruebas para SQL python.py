cursor.execute("CREATE USER (%s) PASSWORD (%s)", ("user", "default_password",))
sql = "CREATE USER %s PASSWORD %s;"


cursor.execute(sql.format('{user}', "{default_password}",))

cursor.execute("CREATE USER %s PASSWORD %s", ["user", "default_password"])

cursor.execute("CREATE USER %s PASSWORD %s", ("user", "default_password"))
