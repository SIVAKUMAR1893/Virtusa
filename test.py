if __name__ == '__main__':
    ############# Add these lines #############
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    ###########################################
    unittest.main()
