def process_data(data):
    print 'Processing user data...'
    for i in xrange(len(data)):
        user = data[i]
        if user.has_key('name'):
            print 'Found user: %s' % user['name']
    print 'Done.'