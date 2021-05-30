import { mount } from '@vue/test-utils'
import ShowImage from '@/components/ShowImage.vue'

describe('ShowImage', () => {
  // コンポーネントがマウントされ、ラッパが作成されます。
  const wrapper = mount(ShowImage)

  it('is exists component', () => {
    expect(wrapper.exists()).toBe(true)
  })

  it('has a button for show image', () => {
    expect(wrapper.find('button').exists()).toBe(true)
  })

  it('has a button for show image', async () => {
    await wrapper.find('button').trigger('click')
    expect(wrapper.find('#resultImage').exists()).toBe(true)
  })
})
