import re
import sys


def main():
    print(parse(input("HTML: ")))
"""
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>
"""

def parse(s):
    if html := re.search(r'^<iframe(?:.*)src="(https?://(?:www\.)?youtube\.com/embed/(.*))"(?:title)*(?:.*)></iframe>$', s):
        html_part = str(html.group(1))
        quote_1st = html_part.find('"')
        if quote_1st != -1:
            x = slice(quote_1st)
            youtube_before = html_part[x]
            if youtube_before:
                if youtube_before.startswith("http:"):
                    youtube_http = re.sub(r"http", "https", youtube_before)
                    youtube_youtu_be = re.sub(r"youtube", "youtu.be", youtube_http)
                    youtube_com = re.sub(r"\.com", "", youtube_youtu_be)
                    youtube_www = re.sub(r"www\.", "", youtube_com)
                    youtube_simple = re.sub(r"embed/", "", youtube_www)

                else:
                    youtube_youtu_be = re.sub(r"youtube", "youtu.be", youtube_before)
                    youtube_com = re.sub(r"\.com", "", youtube_youtu_be)
                    youtube_www = re.sub(r"www\.", "", youtube_com)
                    youtube_simple = re.sub(r"embed/", "", youtube_www)

        else:
            if html_part:
                if html_part.startswith("http:"):
                    youtube_http = re.sub(r"http", "https", html_part)
                    youtube_youtu_be = re.sub(r"youtube", "youtu.be", youtube_http)
                    youtube_com = re.sub(r"\.com", "", youtube_youtu_be)
                    youtube_www = re.sub(r"www\.", "", youtube_com)
                    youtube_simple = re.sub(r"embed/", "", youtube_www)

                else:
                    youtube_youtu_be = re.sub(r"youtube", "youtu.be", html_part)
                    youtube_com = re.sub(r"\.com", "", youtube_youtu_be)
                    youtube_www = re.sub(r"www\.", "", youtube_com)
                    youtube_simple = re.sub(r"embed/", "", youtube_www)

    else:
        youtube_simple = "None"

    return youtube_simple





if __name__ == "__main__":
    main()
