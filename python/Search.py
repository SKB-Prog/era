import sys
import requests
from bs4 import BeautifulSoup

page=sys.argv[1]
query=sys.argv[2]

try:
    if page==1:
        url='https://www.hindilinks4u.quest/?s={}'.format(query)
    else:
        url='https://www.hindilinks4u.quest/page/{}/?s={}'.format(page,query)

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
    else:
        print({"status":"failed"}) 



    soup = BeautifulSoup(html, 'html.parser')

    # Create an object array to store the data
    object_array = []

    # Find all <a> tags within the specified <div> with id "post-104197"
    target_divs = soup.find_all('div', {'class': 'item'})
    if target_divs:
        for target_div in target_divs:
            a_tags = target_div.find_all('a')
            img_tags = target_div.find_all('img')

            for a_tag, img_tag in zip(a_tags, img_tags):
            # Extract the href attribute from <a> tags and src attribute from <img> tags
                _id = a_tag.get('href').replace("https://www.hindilinks4u.quest/", "").rstrip('/')
                img_src = img_tag.get('src')
                img_title=a_tag.get('title')

            # Create a dictionary for each entry
                entry = {
                    '_id': _id,
                    'img_src': img_src,
                    'title':img_title
                }

            # Append the entry to the object array
                object_array.append(entry)

    # # Print the object array
    # for entry in object_array:
    #     print(entry)



    span_tag = soup.find('span', {'class': 'pages'})

    # Check if a <span> tag is found
    if span_tag:
        # Get the text content of the <span> tag
        content = span_tag.text.strip()

        # Split the content by spaces and select the last part
        parts = content.split()
        if len(parts) > 0:
            last_part = parts[-1]
        else:
            last_part=1
    else:
        last_part=1

    i_tag = soup.find('i', {'class': 'count'})

    # Check if the <i> tag is found
    if i_tag:
        # Get the text content of the <i> tag
        count = i_tag.text
        
    else:
        count=0
    result={}
    result['pages']=last_part
    result['total_results']=count
    result['data']=object_array
    print(result)

except Exception as e:
    print('err')