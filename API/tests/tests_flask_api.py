# import ipdb
#
# from unittest import TestCase
# from flask import url_for
# from API.__init__ import create_app
#
#
# class TestFlaskBase(TestCase):
#     def setUp(self):
#         """Runs before all tests"""
#         self.app = create_app()
#         self.app.testing = True
#         self.app_context = self.app.test_request_context()
#         self.app_context.push()
#         self.client = self.app.test_client()
#         self.app.db.create_all()
#
#     def tearDown(self):
#         """Runs after all tests"""
#         self.app.db.session.close()
#         self.app.db.drop_all()
#
#     def test_insert_must_return_the_same_payload_set_without_id(self):
#         data = {
#             'name': 'viniciusTest',
#             'email': 'vinicius@Test'
#         }
#         response = self.client.post(url_for('person.insert'), json=data)
#
#         response.json.pop('id')
#
#         self.assertEqual(data, response.json)
#
#     def test_insert_must_return_error_when_payload_is_incomplete(self):
#         data = {
#             'name': 'viniciusTest',
#             # 'email': 'vinicius@Test'
#         }
#         response = self.client.post(url_for('person.insert'), json=data)
#
#         response.json.pop('id')
#
#         self.assertEqual(data, response.json)
