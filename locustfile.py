from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index(self):
        self.client.get("/")

    @task
    def page1(self):
        self.client.get(
            "/uz/jismoniy-shaxslarga/mobil-aloqa/cdma-2503/xizmatlar-1/qisqa-raqamlar")

    @task
    def page2(self):
        self.client.get(
            "/uz/jismoniy-shaxslarga/uy-telefoni/qoshimcha-xizmatlar-15")

    @task
    def page3(self):
        self.client.get(
            "/uz/jismoniy-shaxslarga/iptv-2/kanallar-2")
