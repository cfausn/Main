from django.test import TestCase



class ViewsTestCase(TestCase):
    def testUserLogin(self):
        resp = self.client.get('/Login/')

        self.assertEqual(resp.status_code, 200)

    def testRedirect(self):
        resp = self.client.get('/Login/redirect.html')
        self.assertEqual(resp.status_code, 200)