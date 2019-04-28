#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/27 下午8:15 
# @Author : Gaoxiang Chen
# @Site :  
# @File : 929. Unique Email Addresses.py 
# @Software: PyCharm
# ---------------------

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        # User set to reduce others, and first build new format

        emailSet = set()
        for email in emails:
            local = email.split('@')[0]
            domain = email.split('@')[1]
            newLocal = ''.join(local.split('+')[0].split('.'))
            newEmail = newLocal + '@' + domain
            if newEmail not in emailSet:
                emailSet.add(newEmail)
        return len(emailSet)
