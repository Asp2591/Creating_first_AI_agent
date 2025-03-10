from pathlib import Path
from phi.agent import Agent
from phi.model.google import Gemini
from phi.playground import Playground, serve_playground_app

image_text_agent = Agent(
    model=Gemini(id="gemini-1.5-flash"),
    markdown=True,
    structured_outputs=True,
    parse_response=True,
    
)

app = Playground(agents=[image_text_agent]).get_app()
user_inp=input("Enter whatever you want::")
# Path to the image
image_path = Path(__file__).parent.joinpath("ai.png")
# user_inp=input("Enter :")
# Get a response from the agent
try:
    response = image_text_agent.print_response(
        f"If the user input is not relevant to the image, please reply 'Not relevant input.'\nYou will be provided with an image. Please respond strictly based on the content of the image.{user_inp}",
        images=[str(image_path)]
    )
    print(response)

except Exception as e:
    print(f"Agent error: {str(e)}")

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)


# from phi.agent import Agent

# agent = Agent(system_prompt="Share a 2 sentence story about")
# agent.print_response("Love in the year 12000.")


# app = Playground(agents=[image_text_agent]).get_app()

# if __name__ == "__main__":
#     serve_playground_app("playground:app", reload=True)