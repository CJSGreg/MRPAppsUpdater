from github import Github

g = Github()

repo = g.get_repo("CJSGreg/MRPAppsUpdater")

contents = repo.get_contents("maintained_apps/MRPDashboards")

for content in contents:
    decoded = content.decoded_content

    print(decoded)
