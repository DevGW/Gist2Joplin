![example workflow](https://github.com/DevGW/Gist2Joplin/actions/workflows/python-app.yml/badge.svg)
# Gist2Joplin

Gist2Joplin is a Python script that allows you to gather gists from GitHub and generate Joplin notes. It provides a seamless way to convert gists into Markdown notes, complete with tags and code blocks.

## Installation

### Clone the Repository
```bash
git clone https://github.com/DevGW/Gist2Joplin.git
cd Gist2Joplin
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Obtain a GitHub API Token

Follow these steps to obtain a GitHub API token:

1. Visit the [GitHub Personal Access Tokens](https://github.com/settings/tokens) page.
2. Generate a new token with the appropriate permissions to access your Gists.
3. Copy the generated token and securely store it.

### Configure Gist2Joplin
Copy the `config.json.example` file to `config.json`:
```bash
cp config.json.example config.json
```
Edit the `config.json` file and provide your GitHub username and API token.

## Usage Examples

To use Gist2Joplin, run the following command:
```bash
python gist2joplin.py <api_token>
```



## Usage

To use Gist2Joplin, follow these steps:

1. Install the necessary dependencies.
2. Provide your GitHub API token.
3. Run the script, passing the API token as an argument.
4. Enjoy the generated Joplin notes!

## License

This project is licensed under the [MIT License](LICENSE).

## Song: Gist2Joplin
### Background

The song "Gist2Joplin" was created as a fun and creative way to celebrate the development of the Gist2Joplin Python script. As a team, we wanted to express our enthusiasm and passion for this project through music.

The song was written by our friendly AI assistant as a collaborative effort with the team. It served as a creative outlet to highlight the script's features, functionality, and the collaborative effort that went into its creation.

Music has a unique way of connecting people, and we wanted to share our excitement with the community by presenting the script in a memorable and enjoyable way. We hope that this song adds a touch of joy and inspiration to your experience with Gist2Joplin.

Please sing along and enjoy the rhythm of Gist2Joplin!

### Lyrics

**Verse 1**  
_In the realm of GitHub, where gists reside,  
We embarked on a journey, side by side.  
With Gist2Joplin, a script so profound,  
Let's explore its wonders, let's break it down._  

**Chorus**  
_Oh, Gist2Joplin, a tool we created,  
To gather gists and have them generated.  
With Markdown and tags, it weaves a story,  
Converting gists into notes, in all their glory._  

**Verse 2**  
_At its core, the script starts with initialization,  
Setting up the API connection and authentication.  
With headers and tokens, authorization secure,  
The stage is set for a gist-gathering tour._  

**Chorus**  
_Oh, Gist2Joplin, a tool we created,  
To gather gists and have them generated.  
With Markdown and tags, it weaves a story,  
Converting gists into notes, in all their glory._  

**Bridge**  
_We begin by fetching the user's gists,  
Page by page, as the API assists.  
As each gist is collected, the journey unfolds,  
Building a list of tags, stories yet untold._  

**Verse 3**  
_With the gists in hand, we enter the directories,  
Creating a structure for files, no worries.  
Tags are extracted, lowercase and sorted,  
Duplicates removed, their uniqueness sorted._  

**Chorus**  
_Oh, Gist2Joplin, a tool we created,  
To gather gists and have them generated.  
With Markdown and tags, it weaves a story,  
Converting gists into notes, in all their glory._  

**Verse 4**  
_The essence of each gist is captured with care,  
Markdown content assembled, beyond compare.  
For each file within, a decision is made,  
Whether to include it directly or encase._  

**Chorus**  
_Oh, Gist2Joplin, a tool we created,  
To gather gists and have them generated.  
With Markdown and tags, it weaves a story,  
Converting gists into notes, in all their glory._  

**Outro**  
_With files composed, the gists come alive,  
Saved in the output, a success to strive.  
Gist files generated, a testament to our quest,  
A script that empowers, among the very best._  

**Chorus**  
_Oh, Gist2Joplin, a tool we created,  
To gather gists and have them generated.  
With Markdown and tags, it weaves a story,  
Converting gists into notes, in all their glory._  

**Outro continued**  
_Let us celebrate the script we crafted as one,  
A tool for organization, second to none.  
Gist2Joplin, a melody of code and art,  
A symphony of collaboration, forever in our heart._  


## Contributing

Contributions to Gist2Joplin are welcome! If you find any issues or have suggestions for improvement, please submit an issue or a pull request. Follow these guidelines when contributing:

- Fork the repository and create a new branch for your contribution.
- Ensure your code follows the established coding conventions.
- Write tests for any new functionality or modifications.


Gist2Joplin is distributed under the [MIT License](LICENSE).

### tags: python, github, joplin
