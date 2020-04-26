from mimesis import Text

full_survey_dict = {
    'name': Text().word().title(),
    'topics':
        [
            {
                'topic_name': Text().word(),
                'questions':
                [
                    {
                        'question': Text().sentence() + '?'
                    },
                    {
                        'question': Text().sentence() + '?'
                    },
                ]
            },
            {
                'topic_name': Text().word(),
                'questions':
                [
                    {
                        'question': Text().sentence() + '?'
                    },
                    {
                        'question': Text().sentence() + '?'
                    },
                ]
            }
    ]
}

full_quiz_dict = {
    'name': Text().word().title(),
    'topics':
        [
            {
                'topic_name': Text().word(),
                'questions':
                [
                    {
                        'question_name': Text().sentence() + '?',
                        'answers':
                        [
                            {
                                'answer': Text().answer(),
                                'is_good': True
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            }
                        ]
                    },
                    {
                        'question_name': Text().sentence() + '?',
                        'answers':
                        [
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': True
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            }
                        ]
                    },
                ]
            },
            {
                'topic_name': Text().word(),
                'questions':
                [
                    {
                        'question_name': Text().sentence() + '?',
                        'answers':
                        [
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': True
                            }
                        ]
                    },
                    {
                        'question_name': Text().sentence() + '?',
                        'answers':
                        [
                            {
                                'answer': Text().answer(),
                                'is_good': True
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            },
                            {
                                'answer': Text().answer(),
                                'is_good': False
                            }
                        ]
                    },
                ]
            }
    ]
}
