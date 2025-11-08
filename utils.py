def filter_api_courses(data):
    
    # init a storage variable to hold filtered courses
    published_course = []
    
    # loop through the courses
    for course in data['courses']:
        print(course["is_published"])
        
        # if a course is published push to published courses list
        if course["is_published"] == True:
             published_course.append(course)
        
    # for now print the list for verification
    print(published_course)
        
    
    # print(data)
    return data