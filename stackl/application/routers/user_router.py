from fastapi import APIRouter

router = APIRouter()

##TODO WIP for during authentication rework
# @router.get('')
# def get_hostname():
#     """Returns hostname of the REST API instance"""
#     return utils_hostname()

# @api.route('', strict_slashes=False)
# class Users(StacklApiResource):
#     def get(self):
#         """Returns all users"""
#         logger.info("[Users GET] Received GET for users")
#         users_list = user_manager.get_users()
#         return {"users": users_list}, StatusCode.OK

#     @api.expect(users_field, validate=True)
#     def post(self):
#         """Creates a new user"""
#         logger.info("[Users POST] Received POST request for user")
#         # extract post data from request
#         json_data = request.get_json()
#         logger.info("[Users POST] User json_data: {}".format(json_data))
#         try:
#             user_manager.create_user(json_data)
#             return {'return_code': StatusCode.CREATED, 'message': 'Created'}, StatusCode.CREATED
#         except Exception as e:
#             return {'return_code': StatusCode.CONFLICT, 'message': 'Error: {}'.format(e)}, StatusCode.CONFLICT

# @api.route('/<serial>', strict_slashes=False)
# class UsersSpecific(StacklApiResource):
#     def get(self, serial):
#         """Returns a user with a specific serial"""
#         logger.info("[UsersSpecific GET] Received GET request for user serial {0}".format(serial))
#         return user_manager.get_user_for_serial(serial), 200

#     @api.response(StatusCode.ACCEPTED, 'Deletes a user')
#     def delete(self, serial):
#         """Delete a user with specific serial"""
#         logger.info("[UsersSpecific DELETE] Received DELETE request for user " + str(serial))
#         try:
#             user_manager.delete_user(serial)
#             return {'return_code': StatusCode.ACCEPTED, 'message': 'User marked for delete'}, StatusCode.ACCEPTED
#         except Exception as e:
#             return {'return_code': StatusCode.CONFLICT, 'message': 'Error: {}'.format(e)}, StatusCode.CONFLICT
