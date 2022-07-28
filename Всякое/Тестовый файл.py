def sort_me(courses):
    return sorted(courses, key=lambda x: (int(x.split('-')[1]), x.split('-')[0], len(x.split('-')[0])))


print(sort_me(['aeb-1305', 'site-1305', 'play-1215', 'web-1304', 'site-1304', 'beb-1305']))
