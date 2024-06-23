from git_filter_repo import Filter, RepoFilter

class ChangeAuthorEmail(RepoFilter):
    def __init__(self, old_email, new_name, new_email):
        self.old_email = old_email
        self.new_name = new_name
        self.new_email = new_email

    def rewrite(self, commit, metadata):
        if commit.author_email.decode('utf-8') == self.old_email:
            commit.author_name = self.new_name.encode('utf-8')
            commit.author_email = self.new_email.encode('utf-8')
        if commit.committer_email.decode('utf-8') == self.old_email:
            commit.committer_name = self.new_name.encode('utf-8')
            commit.committer_email = self.new_email.encode('utf-8')

old_email = b'niharika0706@gmail.com'
new_name = b'Niharika Voodem'
new_email = b'harika5991@gmail.com'
filter = ChangeAuthorEmail(old_email, new_name, new_email)
Filter(repo_path='.', commit_callback=filter.rewrite).run()