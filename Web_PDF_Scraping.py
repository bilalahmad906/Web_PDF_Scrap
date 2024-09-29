import os
import urllib.request

import requests
from bs4 import BeautifulSoup


def extract_links(url1):
    contents = requests.get(url1)
    html_content = contents.content
    soup = BeautifulSoup(html_content, 'html.parser')
    anchors = soup.find_all('a')
    all_links = set()

    for link1 in anchors:
        if link1.get('href') != '#' and link1.get('href').endswith('.pdf'):
            link_text = "https://kathrein-bca.com/en/products/kathrein-products/catalogues-and-brochures/" + link1.get(
                'href')
            all_links.add(link_text)

    return all_links


# def download_pdfs(links1, download_folder1):
#     if not os.path.exists(download_folder1):
#         os.makedirs(download_folder1)
#
#     for link in links1:
#         response = requests.get(link)
#         filename = os.path.join(download_folder1, link.split("/")[-1])
#         with open(filename, 'wb') as pdf_file:
#             pdf_file.read(response.content)
#             print(f"Downloaded: {filename}")


if __name__ == "__main__":
    url = "https://kathrein-bca.com/en/products/kathrein-products/catalogues-and-brochures/"
    links = extract_links(url)
    print(links)
    # download_folder = "downloaded_pdfs"
    # download_pdfs(links, download_folder)
