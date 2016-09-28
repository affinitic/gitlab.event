# -*- coding: utf-8 -*-
"""
github.event

Licensed under the GPL license, see LICENCE.txt for more details.
"""
from git.event.request import GitPullRequest, GitPushRequest


class GitLabPullRequest(GitPullRequest):

    @property
    def base_repo_url(self):
        return self.json_body['object_attributes']['target']['git_http_url']

    @property
    def base_repo_name(self):
        return self.json_body['object_attributes']['target']['name']

    @property
    def head_repo_url(self):
        return self.json_body['object_attributes']['source']['git_http_url']

    @property
    def head_repo_name(self):
        return self.json_body['object_attributes']['source']['name']


class GitLabPushRequest(GitPushRequest):

    @property
    def base_repo_url(self):
        return self.json_body['project']['git_html_url']

    @property
    def base_repo_name(self):
        return self.json_body['project']['name']

    @property
    def commits(self):
        return [GitLabCommit(commit_body) for commit_body in self.json_body['commits']]

    @property
    def author(self):
        return self.json_body['user_name']


class GitLabCommit(object):

    def __init__(self, commit_body):
        self.commit_body = commit_body

    @property
    def id(self):
        return self.commit_body['id']

    @property
    def branch(self):
        # XXX tester commit dans autre branch
        return "master"

    @property
    def username(self):
        return self.commit_body['author']['name']

    @property
    def message(self):
        return self.commit_body['message']

    @property
    def timestamp(self):
        return self.commit_body['timestamp']

    @property
    def url(self):
        return self.commit_body['url']
