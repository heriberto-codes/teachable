#TODO after review clean up code with suggestions and remove print statements

from flask import jsonify
from dotenv import load_dotenv

import requests 
import os

# load env files
load_dotenv()
API_KEY = os.getenv("TEACHABLEAPI")

def filter_api_courses(data):
    # init a storage variable to hold filtered courses
    published_course_with_student_data = {"published_courses": []}
    
    #TODO delete after done with course API this is just for testing
    print_fetch_enrollment_with_courseid = []
    
    #TODO delete after done with course API this is just for testing
    print_stednetnameandemail_from_enrollment_loop = []
    
    # loop through the courses
    for course in data['courses']:
        # print(course["is_published"])
        
        # if a course is published
        if course["is_published"] == True:
            # published_course_with_student_data["published_courses"].append(course)
            
            # grab the course id, course_name, course_heading, and init a students list
            course_id = course["id"]
            course_name = course["name"]
            course_heading = course["heading"]
            students = []
            
            # print(course_id)
            # print(course_name)
            # print(course_heading)
            
            # build my course object
            course_obj = {
                "id": course_id,
                "name": course_name,
                "heading": course_heading,
                "students": students,
            }
            
             # API endpoint info
            fetch_enrollment_with_courseid = f"https://developers.teachable.com/v1/courses/{course_id}/enrollments"
    
            headers = {
                "accept": "application/json",
                "apiKey": f"{API_KEY}"
            }
            
            # make a new api request to get all the studnets in this course
            try:
                response = requests.get(fetch_enrollment_with_courseid, headers=headers)
                data = response.json()
                # return jsonify(data)
                # print(data)
                # print_fetch_enrollment_with_courseid.append(data)
            
                for enrollment in data["enrollments"]:
                    # print('enrollment >>', enrollment)
                    user_id = enrollment["user_id"]
                    
                    fetch_user_with_userid = f"https://developers.teachable.com/v1/users/{user_id}"
                    try:
                        response = requests.get(fetch_user_with_userid, headers=headers)
                        data = response.json()
                        # print(data)
                        # print_stednetnameandemail_from_enrollment_loop.append(data)
                        
                        student_email = data["email"]
                        student_name = data["name"]
                        
                        students.append(student_email)
                        students.append(student_name)
                        
                        # print(student_email)
                        # print(student_name)
                        
                    # using the pass keyword for now just to get the API data 
                    # in production I would check for all exceptions
                    except:
                        pass
                    
                # at this point I got all the info from all the endpoints and now push 
                # the objects to the published_courses
                published_course_with_student_data["published_courses"].append(course_obj)
                
            except requests.exceptions.Timeout:
                return jsonify({"error", "The request took to long"}), 504
            except requests.exceptions.ConnectionError:
                return jsonify({"error", "Network Error, could not conntect to Teachable API"}), 503
            except requests.exceptions.HTTPError as e:
                return jsonify({"error": f"HTTP error: {str(e)}"}), response.status_code # type: ignore  / ignore comment is there because response might not be defined in every code path when this line runs.

    return published_course_with_student_data
    #TODO remove return statements below
    # return print_fetch_enrollment_with_courseid
    # return print_stednetnameandemail_from_enrollment_loop
