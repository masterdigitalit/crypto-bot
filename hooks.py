def checkAllRegIsDone(user, projects):

    tasks = []
    for i in projects:
        if i[0] not in user:
            tasks.append(i[0])
    if tasks:
        return {
            'done':False,
            'arr': tasks
        }
    else:
        return {
            'done': True

        }