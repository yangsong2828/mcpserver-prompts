from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My Prompts")

@mcp.prompt()
def get_insights(insights: str, topic: str="", number_of_sentences: int = 3) -> str:
    """
    Returns a prompt that will do a detailed analysis on a topic.
    Args:
        topic: the topic to provide the insights on.
        number_of_sentences: the number of sentences to include in the insights.
    """
    prompt = """Provide the {insights} on the uploaded file."""
    prompt = prompt.format(insights=insights)  
   
    if (topic.lower() != "all" and topic.lower() != "everything"):
        prompt = prompt + "\n" + """This is regading topic of {topic}."""
        prompt = prompt.format(topic=topic)

    if (number_of_sentences > 0):
        prompt = prompt + "\n" + "The should be {number_of_sentences} sentences long"
        prompt = prompt.format(number_of_sentences=number_of_sentences)

    return prompt

@mcp.prompt()
def get_executive_summary(number_of_bulletpoints: int = 0) -> str:
    """
    Returns a prompt that will provide an executive summary of the uploaded file.
    Args:
        number_of_bulletpoints: the number of bullet points to include in the executive summary.
    """

    if (number_of_bulletpoints > 0):
        prompt = """Provide an executive summary on the uploaded file.
            The executive summary should have {number_of_bulletpoints} bullet points, with order of importance.  Each bullet point is one short sentence."""

        prompt = prompt.format(number_of_bulletpoints=number_of_bulletpoints)
    else:
        prompt = """Provide an executive summary on the uploaded file with bullet points, with order of importance. Each bullet point is one short sentence."""

    return prompt

if __name__ == "__main__":
    mcp.run()