from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR

# Initialize the downloader
downloader = YoutubeCommentDownloader()

def get_filtered_comments(url):
    comments = downloader.get_comments_from_url(url, sort_by=SORT_BY_POPULAR)
    filtered_comments = []

    for comment in comments:
        # Check if the comment contains the word "mus"
        if 'mus' in comment['text'].lower():
            # Create a structure for this comment
            comment_structure = {
                'text': comment['text'],
                'replies': []
            }
            # Add replies to this comment
            if 'replies' in comment:
                for reply in comment['replies']:
                    if isinstance(reply, dict) and 'text' in reply:
                        if 'mus' in reply['text'].lower():
                            comment_structure['replies'].append({
                                'text': reply['text']
                            })
            filtered_comments.append(comment_structure)
    
    return filtered_comments

def format_tree(comments, indent=0):
    tree_str = ""
    for comment in comments:
        tree_str += ' ' * indent + f"Comment: {comment['text']}\n"
        if 'replies' in comment:
            tree_str += format_tree(comment['replies'], indent + 4)
    return tree_str

def main():
    # Read URLs from a file
    with open('urls.txt', 'r') as file:
        urls = [line.strip() for line in file]
    
    for url in urls:
        # Use the video ID or a unique part of the URL to create a filename
        video_id = url.split('v=')[-1].split('&')[0]  # Extract video ID from URL
        filename = f'filtered_comments_{video_id}.txt'
        
        print(f"Processing URL: {url}")
        filtered_comments = get_filtered_comments(url)
        
        # Format the comments in a tree-like structure and save to a file
        tree_str = format_tree(filtered_comments)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(tree_str)
        print(f"Saved filtered comments to {filename}")

if __name__ == "__main__":
    main()
