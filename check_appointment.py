# Goal: Checks for available visa appointment slots on the Greece MFA website.

import asyncio
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, SecretStr

from browser_use.agent.service import Agent
from browser_use.controller.service import Controller


# Load environment variables
load_dotenv()
if not os.getenv('OPENAI_API_KEY'):
    raise ValueError('OPENAI_API_KEY is not set. Please add it to your environment variables.')

controller = Controller()


class WebpageInfo1(BaseModel):
	"""Model for webpage link."""
	link: str = 'https://njac.clubautomation.com/'


@controller.action('Go to the webpage', param_model=WebpageInfo1)
def go_to_webpage1(webpage_info: WebpageInfo1):
	"""Returns the webpage link."""
	return webpage_info.link


async def main():
	
	"""Main function to execute the agent task."""
	task = (
		'Go to the njac.clubautomation.com webpage via the link I provided you.'
		'use knatarajan as USERNAME and NJAC1234 as password, then click on Login'
		'Click Reserve a Court'
		'Click on plus icon of Add Participant, Type Venkat Tata,  chose Venkat Tata in autocomplete list'
		'Click on 120 mins'
		'Choose 11:00am and wait for few seconds to load the pop screen with confirm button'
		'Choose Confirm for the booking'
	)

	model = ChatOpenAI(model='gpt-4o-mini', api_key=SecretStr(os.getenv('OPENAI_API_KEY', '')))
	agent = Agent(task, model, controller=controller, use_vision=True)
	

	await agent.run()


if __name__ == "__main__":
	asyncio.run(main())