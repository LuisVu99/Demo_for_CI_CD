import allure

class AllureHelper():
    @staticmethod
    def attach_screenshot(page, name = "screenshot"):
        allure.attach(
            page.screenshot(full_page=True),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @staticmethod
    def attach_text(name, content):
        allure.attach(
            content,
            name=name,
            attachment_type=allure.attachment_type.TEXT
        )

    @staticmethod
    def attach_video(path, name = "Video"):
        with open(path, "rb") as f:
            allure.attach(
                f.read(),
                name = name,
                attachment_type = allure.attachment_type.MP4
            )