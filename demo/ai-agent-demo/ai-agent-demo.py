import os
import tools
from pathlib import Path
from pydantic_ai import Agent
from dotenv import load_dotenv

load_dotenv()

class tools:
    def __init__(self):
        self.base_dir = Path("./test")
        pass

    def read_file(self, name: str) -> str:
        print(f"(read_file) {name}")
        try:
            with open(self.base_dir / name, "r") as f:
                content: str = f.read()
            return content
        except Exception as e:
            return f"An error occurred: {e}"
    def list_files(self) -> list[str]:
        print("(list_file)")
        file_list = []
        for item in self.base_dir.rglob("*"):
            if item.is_file():
                file_list.append(str(item.relative_to(self.base_dir)))
        
        return file_list
    
    def rename_file(self, name: str, new_name: str) -> str:
        print(f"(rename_file {name} -> {new_name})")
        
        try:
            new_path = self.base_dir / new_name
            if not str(new_path).startswith(str(self.base_dir)):
                return "Error: new_name is outside base_dir."
            os.makedirs(new_path.parent, exist_ok=True)
            os.rename(self.base_dir / name, new_path)
            
            return f"File '{name}' successfully renamed to '{new_name}'"
        except Exception as e:
            return f"An error occurred: {e}"
# 初始化实例
tools = tools()

agent = Agent(
    "google-gla:gemini-2.5-pro-preview-05-06",
    system_prompt = "You are an experienced programmer",
    # 告诉 AI 用哪些功能函数
    tools=[tools.read_file(), tools.list_files(), tools.rename_file()]
)


def main():
    history = []
    while True:
        user_input = input("input:")
        resp = agent.run_sync(user_input, message_history=history)

        history = list(resp.all_messages())
        print(resp.output)

if __name__ == "__main__":
    main()
