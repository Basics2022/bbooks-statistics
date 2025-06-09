import os
import glob
import yaml

# Find post files
post_files = sorted(glob.glob("posts/*.md"), reverse=True)[:5]


index_content = "(blog)=\n# basics blog\n\n"

index_content += "## Latest Posts\n\n"

for post_file in post_files:
    with open(post_file, "r") as f:
        lines = f.readlines()

    # Parse frontmatter
    if lines[0].strip() == "---":
        end_idx = lines[1:].index("---\n") + 1
        frontmatter = yaml.safe_load("".join(lines[1:end_idx]))
        title = frontmatter.get("title", os.path.basename(post_file))
        date = frontmatter.get("date", "")
    else:
        title = os.path.basename(post_file)
        date = ""

    preview_line = 10
    preview = "".join(lines[preview_line+1: preview_line+5])  # First few lines of content

    post_link = post_file.replace(".md", "")

    index_content += f"### [{title}]({post_link})\n*{date}*\n\n{preview}\n\n---\n\n"

# Save index.md
with open("index.md", "w") as f:
    f.write(index_content)
