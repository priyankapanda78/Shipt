import unittest
import requests
import json

class starwars(unittest.TestCase):

#Q1 Assert that Obi-Wan Kenobi was in the film A New Hope
    def testName(self):
        self.film = requests.get('https://swapi.co/api/films/')
        self.response = self.film.json()
        self.assertEqual(self.film.status_code,200)
        charName=[]
        for i in range(0,len(self.response['results'])):
            if self.response['results'][i]['title'] == 'A New Hope': #checking the title 'A New Hope' for films

                for i in range(0,len(self.response['results'][0]['characters'])):
                    self.characters = requests.get(self.response['results'][0]['characters'][i])
                    self.name = self.characters.json()
                    charName.append(self.name['name']) #All the characters for film stored in charName
        self.assertIn("Obi-Wan Kenobi",charName) #Validating for movie 'A New Hope', character 'Obi-Wan Kenobi' is in charName.

#Q2 Assert that the Enterprise is a starship (yes, this should fail)
    def testEnterprise(self):
        page = 1
        url = "https://swapi.co/api/starships/?page="
        listOfships = []
        while True:
            self.starship = requests.get(url+str(page))
            self.assertEqual(self.starship.status_code, 200)
            self.response = self.starship.json()
            for i in range(0, len(self.response['results'])):  #All the starships name are stored in listOfShips navigating through all the pages
                self.ship = self.response['results'][i]['name']
                listOfships.append(self.ship)
            if self.response['next'] is None:
                break
            page = page + 1

        self.assertIn('Enterprise', listOfships)

#Q3  Assert that Chewbacca is a Wookie
    def testWookie(self):
        page = 1
        url = "https://swapi.co/api/people/?page="
        new = []
        while True:
            self.people = requests.get(url + str(page))
            self.assertEqual(self.people.status_code,200)
            self.response = self.people.json()
            chewbaccaFound = False
            for i in range(0, len(self.response['results'])):
                if self.response['results'][i]['name'] == 'Chewbacca': #Verifying the people name is 'Chewbacca'
                    url1 = self.response['results'][i]['species']
                    url1 = str(url1)[1:-1]
                    url1 = url1.replace("'", "")
                    self.species = requests.get(url1)  #Species api is hit for validation
                    self.wookie = self.species.json()
                    self.assertEqual(self.wookie['name'],"Wookiee")
                    chewbaccaFound = True
                    break
            if self.response['next'] is None:
                break
            page = page + 1
            if chewbaccaFound:
                break

#Q4 Assert that the /starships endpoint returns the fields:
    def testStarships(self):
        self.starship = requests.get("https://swapi.co/api/starships/")
        self.assertEqual(self.starship.status_code,200)
        self.response = self.starship.json()
        fields = []

        assert (len(self.response['results']) > 1)

        for key in self.response['results'][0]:
            if key == 'name':
                fields.append(key)
            elif key == 'model':
                fields.append(key)
            elif key == 'crew':
                fields.append(key)
            elif key == 'hyperdrive_rating':
                fields.append(key)
            elif key == 'pilots':
                fields.append(key)
            elif key == 'films':
                fields.append(key)
            else:
                pass

        self.assertEqual(len(fields), 6) #Validating the size of fields list
        self.assertIn('model', fields)
        self.assertIn('name',fields)
        self.assertIn('crew',fields)
        self.assertIn('hyperdrive_rating',fields)
        self.assertIn('pilots',fields)
        self.assertIn('films',fields)

 #Q5 Assert that the /starships count returned is correct by paging through the results
    def testStarshipsCount(self):
        page = 1
        url = "https://swapi.co/api/starships/?page="
        starships_count = 0
        while True:
            self.starship = requests.get(url + str(page))
            self.assertEqual(self.starship.status_code, 200)
            self.response = self.starship.json()
            for j in range(0,len(self.response['results'])):
                starships_count+=1
            if self.response['next'] is None:
                    break
            page = page + 1
        self.assertEqual(starships_count, self.response['count']) #Validating the total count of ships
