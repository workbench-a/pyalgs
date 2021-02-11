import pytest
from pyalgs.sort import insertion

@pytest.fixture(scope="module", params=[[[],[]], [[1,1,1,1],[1,1,1,1]], [[-1,-2,4,-3],[-3,-2,-1,4]], [[3,5,1],[1,3,5]]])
def arr_sample(request):
    yield request.param

@pytest.fixture(scope="module", params=[[[],[],[]], [[],[1], [1]], [[-1],[-2], [1,-2]],[[-3,-2,-1,4], [3,5,1],[-3, -2, -1, 4, 3, 5, 1]]])
def arr_merge_sample(request):
    yield request.param

def test_insertion(arr_sample):
    assert insertion(arr_sample[0]) == arr_sample[1]

# def test_selection_sort(arr_sample):
#     assert sort2.selection_sort(arr_sample[0]) == arr_sample[1]

# def test_merge(arr_sample):
#     assert sort2.merge(arr_merge_sample[0], arr_merge_sample[1]) == arr_merge_sample[2]

# def test_merge_sort(arr_sample):
#     assert sort2.merge_sort(arr_sample[0]) == arr_sample[1]

# def test_bubble_sort(arr_sample):
#     assert sort2.selection_sort(arr_sample[0]) == arr_sample[1]

# def test_short_bubble_sort(arr_sample):
#     assert sort2.selection_sort(arr_sample[0]) == arr_sample[1]

# def test_quick_sort(arr_sample):
#     assert sort2.selection_sort(arr_sample[0]) == arr_sample[1]

# def test_shell_sort(arr_sample):
#     assert sort2.selection_sort(arr_sample[0]) == arr_sample[1]