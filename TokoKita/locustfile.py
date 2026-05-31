from locust import HttpUser, task, between

class TokoKitaUser(HttpUser):
    # Set wait time dynamically between 1 to 3 seconds
    wait_time = between(1, 3)

    @task(4)  # 80% weight
    def view_catalogue(self):
        self.client.get("/catalogue")

    @task(1)  # 20% weight
    def checkout(self):
        self.client.post("/checkout")
