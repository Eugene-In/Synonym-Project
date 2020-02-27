class DataManager:

    def manager(dodge):
        bullet = {}
        for x in dodge:
            if x in bullet:
                bullet[x] = bullet[x]+1
            else:
                bullet[x] = 1
        return bullet
