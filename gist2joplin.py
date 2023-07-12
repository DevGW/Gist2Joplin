import json
import os
import re
from sys import argv
import requests

class Gist2Joplin:
    # __init__(self, config) method
    # @description Initializes the Gist2Joplin class
    # @param self
    # @param config: The configuration object
    # @return void
    def __init__(self, config):
        self.api_token = config['api_token']
        self.api_url = f"https://api.github.com/gists?per_page=50&"
        self.gists = []
        self.tags = []
        self.categorized_dict = {}
        self.headers = {
            'Authorization': 'Bearer ' + self.api_token,
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }

    # Start(self) method
    # @description Starts the Gist2Joplin script
    # @param self
    # @return void
    def Start(self):
        ### get gists
        self.get_gists()
        ### build tag list
        self.buildTagListDirectories()

    # get_gists(self) method
    # @description Gets all the gists from the GitHub API
    # @param self
    # @return void
    def get_gists(self):
        page = 1
        gists = None
        current_page_url = None
        next_page_url = self.api_url # + f"page={page}"
        # while gists or page <= 50:
        while current_page_url != next_page_url:
            current_page_url = next_page_url
            print(f"Getting gists page: {page}")
            res = requests.get(next_page_url, headers=self.headers)
            gists = res.json()
            self.gists += gists
            page += 1

            # Check if the 'link' header is present in the response
            if 'link' in res.headers:
                link_header = res.headers['link']

                # Extract URLs and their corresponding relations from the link header
                links = re.findall(r'<(.*?)>; rel="(.*?)"', link_header)
                # Find the 'next' page URL
                for link, rel in links:
                    if rel == 'next':
                        next_page_url = link

        return self.gists

    # buildTagListDirectories(self) method
    # @description Builds the tag list directories
    # and the Markdown files for each gist
    # then saves them to the output directory
    # @param self
    # @return void
    def buildTagListDirectories(self, base_dir=os.getcwd()):
        print("Building directories and Markdown files...")
        content_dir = os.path.join(base_dir, "output", "gists")
        os.makedirs(content_dir, exist_ok=True)
        for gist in self.gists:
            # Check if the gist is public
            # if not gist["public"]:
            #     continue

            tags_with_prefix = re.findall(r'\#\w+', gist['description'])
            tags = [tag[1:].lower() for tag in tags_with_prefix]

            # Remove duplicates and sort the tags
            tags = list(set(tags))
            tags.sort(key=str.casefold)

            # Extract the gist name from the description and replace multiple spaces with a single space
            gist_name = re.sub(r'#\w+\s*', '', gist['description']).strip()
            gist_name = re.sub(r'\s{2,}', ' ', gist_name)

            # Create the Markdown content for the gist
            markdown_content = ""
            for file_name, file_data in gist["files"].items():
                # Retrieve the raw content of the file
                raw_url = file_data["raw_url"]
                response = requests.get(raw_url)
                content = response.text

                # Determine the file extension
                _, file_extension = os.path.splitext(file_name)

                if file_extension == ".md":
                    # If the file is already a markdown file, include its content directly without the code block
                    markdown_content += f"{content}\n\nTags: {' '.join(f'#{tag}' for tag in tags)}\n\n"
                else:
                    # Add the code block for the file
                    markdown_content += f"{file_name}\n\n```{file_data['language']}\n{content}\n```\n\nTags: {' '.join(f'#{tag}' for tag in tags)}\n\n"

            # Replace any number of spaces with a single space
            gist_name = re.sub(r'\s+', ' ', gist_name)

            # Remove all non-alphanumeric characters or underscores
            gist_name = re.sub('[^A-Za-z0-9_ ]+', '', gist_name[0:50])

            # Generate the filename based on the gist name
            file_name = f"{gist_name}.md"

            # Write the Markdown content to the output/gists directory
            file_path = os.path.join("output", "gists", file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(markdown_content)

            print(f"Saved gist file: {file_path}")

        print("Gist files generated successfully.")


# procArgs(args) method
# @param args: command line arguments
# @return: None
def procArgs(args):
    if len(args) > 1:
        print(f"Usage: {args[0]}")
        exit()

    config_file_path = "./config.json"
    if not os.path.isfile(config_file_path):
        print("Error: config.json file not found.")
        exit()

    with open(config_file_path, "r") as config_file:
        config = json.load(config_file)

    ### instantiate class
    gt = Gist2Joplin(config)
    print("Starting Gist2Joplin...")
    gt.Start()

if __name__ == '__main__':
    procArgs(argv)

