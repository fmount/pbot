#!/usr/bin/env python

gerrit_config = {
    'instance': 'review.openstack.org',
    'port': '29418',
    'mode': 'ssh',
    'submissions': {
        '778915': {
            'actions': [
                'watch',
                'rebase',
                'recheck'
            ]
        },
        '780794': {
            'actions': [
                'watch'
            ]
        },
        '781069': {
            'actions': [
                'watch'
            ]
        }
    },
    'allowed_ci': [
        'Zuul',
        'RDO Third Party CI'
    ],
    'user': {
        'name': 'cephbot',
        'psw': 'None',
        'key': '<path_of_the_cephbot_private_key>'
    },
    'pending_ceph': '778915'
}

irc = {
    'server': 'chat.freenode.net',
    'port': '6667',
    'nick': 'cephbot',
    "pass": "cephbot",
    'channels': [
        '#tripleo-ceph2',
    ],
    'allowed_nicks': [
        'fmount'
    ],
    'log': 'cephbot.log',
    'callback': [
        'hello',
        'help',
        'gerrit',
        'guess',
        'squad'
    ]
}
