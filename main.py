from trelloapp.trello_app import TrelloApp



#KAKO SAKRITI OVE PODATKE?


API_KEY='882a3299e3be109c4baeca86bd7f9f5e'
API_TOKEN='ATTAe2339fc18de1cd1f7b71dd3705610cf92a5e83c55da4928bc74fd6c0d216fdee4D596758'
BOARD_ID='6643da406a3e2b29e3472a90'


#KAKO SAKRITI OVE PODATKE?
    

def main():
    app = TrelloApp(API_KEY, API_TOKEN, BOARD_ID)
    app.run()

if __name__ == "__main__":
    main()
