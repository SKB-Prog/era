import sys
import requests
from bs4 import BeautifulSoup

_id=sys.argv[1]

try:
    url = 'https://www.hindilinks4u.quest/{}/'.format(_id)
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
    else:
        print('Failed to retrieve the webpage') 

    soup = BeautifulSoup(html, 'html.parser')

    detail = soup.find('div', {'class':'entry-content'})
    video_tabs=soup.find('ul',{'id':'video_tabs'})
    a_tags = video_tabs.find_all('a')

        # Extract href values and store them in an array
    videos_arr = [a.get('href') for a in a_tags]

    object_array = []

    target_divs = soup.find_all('div', {'class': 'item'})
    if target_divs:
        for target_div in target_divs:
            a_tags = target_div.find_all('a')
            img_tags = target_div.find_all('img')

            for a_tag, img_tag in zip(a_tags, img_tags):
            # Extract the href attribute from <a> tags and src attribute from <img> tags
                _id = a_tag.get('href').replace("https://www.hindilinks4u.quest/", "").rstrip('/')
                img_src = img_tag.get('data-src')
                img_title=a_tag.get('title')

            # Create a dictionary for each entry
                entry = {
                    '_id': _id,
                    'img_src': img_src,
                    'title':img_title
                }

            # Append the entry to the object array
                object_array.append(entry)


    img_tag = detail.find('img')
    imageUrl = img_tag.get('data-src')

    # Extract movieName from the h2 tag
    h2_tag = detail.find('h2')
    movieName = h2_tag.text.strip()

    # Extract descrip from all p tags


    # Find all <strong> tags
    strong_tags = detail.find_all('strong')

    # Create an array to store the dictionaries
    data_array = []

    # Loop through the <strong> tags
    for strong_tag in strong_tags:
        # Get the text from the <strong> tag as the key
        key = strong_tag.text.strip()

        # Find the following <p> tag
        p_tag = strong_tag.find_parent('p')

        # Check if a <p> tag is found
        if p_tag:
            # Get the text from the <p> tag as the value
            value = p_tag.text.strip()

            # Remove the <strong> tag's contents from the <p> tag's contents
            value = value.replace(key, '').strip()

            # Create a dictionary with the key and value
            data = {key: value}

            # Append the dictionary to the array
            data_array.append(data)

    # Print the array of dictionaries
    Data_object = {}

    # Loop through the array of objects and merge them into one object
    for obj in data_array:
        Data_object.update(obj)




    Data_object.pop(':',None)


    # Create an object to store the extracted data
    data_object = {
        'imageUrl': imageUrl,
        'movieName': movieName,
    }
    Data_object.update(data_object)

    Data_object['vidoes_url']=videos_arr




    Data_object['relatedPost']=object_array
    print(Data_object)

except Exception as e:
    print("err")